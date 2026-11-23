/**
 * The New note screen: the choices the Supernote asks for when you make a note
 * (name, folder, page style, handwriting recognition, orientation), opened from a
 * New note button. Create makes the notebook and opens it.
 */
import React, {useEffect, useState} from 'react';
import {Image, ScrollView, Text, TextInput, TouchableOpacity, View} from 'react-native';

import {DockItem} from './config';
import {Btn, Choice, PathPicker, st, T} from './hubsettings';
import {createNote, myTemplates, stampName, systemTemplates} from './open';

const INK = '#000000';
const ROOT = '/storage/emulated/0';
const short = (p: string) => p.replace(ROOT, '').replace(/^\//, '') || 'Internal storage';
const styleName = (t: string) =>
  t.startsWith('/') ? t.substring(t.lastIndexOf('/') + 1).replace(/\.(png|jpe?g|webp)$/i, '') : t.replace(/^style_/, '').replace(/_/g, ' ');

export function NewNoteScreen({d, onClose}: {d: Extract<DockItem, {kind: 'create'}>; onClose: () => void}) {
  const [name, setName] = useState(stampName());
  const [folder, setFolder] = useState(d.folder);
  const [template, setTemplate] = useState<string | undefined>(d.template);
  const [recognition, setRecognition] = useState(!!d.recognition);
  const [landscape, setLandscape] = useState(!!d.landscape);
  const [picking, setPicking] = useState<'folder' | 'style' | null>(null);
  const [system, setSystem] = useState<string[] | null>(null);
  const [mine, setMine] = useState<string[] | null>(null);
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    if (picking === 'style' && system === null) {
      systemTemplates().then(setSystem);
      myTemplates().then(setMine);
    }
  }, [picking, system]);

  if (picking === 'folder') return <PathPicker mode="folder" start={folder} onClose={() => setPicking(null)} onPick={p => (setFolder(p), setPicking(null))} />;

  if (picking === 'style')
    return (
      <View style={{flex: 1, backgroundColor: '#ffffff', padding: 20}}>
        <View style={{flexDirection: 'row', alignItems: 'center', marginBottom: 14}}>
          <Text style={{fontSize: T.title, fontWeight: '700', color: INK, flex: 1}}>Page style</Text>
          <Btn label="Cancel" onPress={() => setPicking(null)} />
        </View>
        <ScrollView style={{flex: 1}}>
          {mine && mine.length > 0 && <Text style={st.label}>Your templates (MyStyle)</Text>}
          <View style={{flexDirection: 'row', flexWrap: 'wrap'}}>
            {mine?.map(p => (
              <TouchableOpacity
                key={p}
                onPress={() => (setTemplate(p), setPicking(null))}
                style={{width: '25%', padding: 8, alignItems: 'center', borderWidth: p === template ? 3 : 0, borderColor: INK, borderRadius: 10}}>
                <Image source={{uri: 'file://' + p}} style={{width: '100%', aspectRatio: 0.75, borderWidth: 1, borderColor: '#999999'}} resizeMode="cover" resizeMethod="resize" fadeDuration={0} />
                <Text style={{fontSize: 15, color: INK, marginTop: 4}} numberOfLines={2}>
                  {styleName(p)}
                </Text>
              </TouchableOpacity>
            ))}
          </View>
          <Text style={st.label}>Supernote styles</Text>
          {system === null && <Text style={st.p}>loading…</Text>}
          {system?.map(n => (
            <TouchableOpacity
              key={n}
              onPress={() => (setTemplate(n), setPicking(null))}
              style={{minHeight: 64, justifyContent: 'center', borderBottomWidth: 1, borderColor: '#cccccc'}}>
              <Text style={{fontSize: T.body, color: INK}}>
                {n === template ? '✓ ' : ''}
                {styleName(n)}
              </Text>
            </TouchableOpacity>
          ))}
        </ScrollView>
      </View>
    );

  return (
    <View style={{flex: 1, backgroundColor: '#ffffff'}}>
      <View style={{flexDirection: 'row', alignItems: 'center', paddingHorizontal: 20, paddingTop: 14, paddingBottom: 10, borderBottomWidth: 2, borderColor: INK}}>
        <Text style={{fontSize: T.title, fontWeight: '700', color: INK, flex: 1}}>New note</Text>
        <Btn label="Cancel" onPress={onClose} />
      </View>
      <ScrollView style={{flex: 1}} contentContainerStyle={{padding: 20}} keyboardShouldPersistTaps="handled">
        <Text style={st.label}>Name</Text>
        <TextInput
          value={name}
          onChangeText={setName}
          selectTextOnFocus
          showSoftInputOnFocus
          autoCorrect={false}
          placeholder="Name of the note"
          placeholderTextColor="#999999"
          style={{minHeight: 68, fontSize: 24, borderWidth: 1.5, borderColor: '#c8c8c8', borderRadius: 18, paddingHorizontal: 18, color: INK}}
        />

        <Text style={st.label}>Folder</Text>
        <View style={st.row}>
          <Text style={{fontSize: T.body, color: INK, marginRight: 14}}>{short(folder)}</Text>
          <Btn label="Change" onPress={() => setPicking('folder')} />
        </View>

        <Text style={st.label}>Page style</Text>
        <View style={st.row}>
          <Text style={{fontSize: T.body, color: INK, marginRight: 14}}>{template ? styleName(template) : 'Plain white'}</Text>
          <Btn label="Change" onPress={() => setPicking('style')} />
        </View>

        <Text style={st.label}>Handwriting recognition while you write</Text>
        <Choice options={[{v: 'off', label: 'Off'}, {v: 'on', label: 'On'}]} value={recognition ? 'on' : 'off'} onChange={v => setRecognition(v === 'on')} />

        <Text style={st.label}>Orientation</Text>
        <Choice options={[{v: 'p', label: 'Portrait'}, {v: 'l', label: 'Landscape'}]} value={landscape ? 'l' : 'p'} onChange={v => setLandscape(v === 'l')} />

        <View style={[st.row, {marginTop: 24}]}>
          <Btn
            primary
            disabled={busy || !name.trim()}
            label={busy ? 'Making…' : 'Create'}
            onPress={async () => {
              setBusy(true);
              const ok = await createNote(folder, template, recognition, name.trim(), landscape);
              setBusy(false);
              if (ok) onClose();
            }}
          />
          <Btn label="Cancel" onPress={onClose} />
        </View>
      </ScrollView>
    </View>
  );
}
